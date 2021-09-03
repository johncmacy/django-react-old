import React from 'react'
import Button from './components/Button'

export default function App() {
  return (
    <div>
      <h1>App</h1>
      <Button text="Click me" onClick={(e) => alert("hello")} />
    </div>
  )
}