const path = require('path');

module.exports = {
  mode: 'development',
  entry: './frontend/index.js',
  output: {
    filename: 'frontend-build.js',
    path: path.resolve(__dirname, './project/static/js'),
    publicPath: '/static/js/',
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        loader: "babel-loader",
        options: {
          presets: ["@babel/preset-env", "@babel/preset-react"]
        }
      }
    ]
  },
  devServer: {
    hot: true,
    port: 8080,
    proxy: {
      '!/static/frontend/**': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      }
    }
  }
};