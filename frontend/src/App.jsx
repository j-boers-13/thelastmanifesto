import React, {Component} from 'react'
import MessageList from './Components/MessageList'
import Navbar from './Components/Navbar'
import { BrowserRouter as Router, Route, Link, Switch, Redirect} from 'react-router-dom'
import Container from './Components/Container'

export default class App extends Component {

  constructor() {
    super()
    this.state = {
      messages: 'hello'
    }
  }
  render() {
    return(
        <Router>
          <div id="container">
            <Navbar />
            <Container />
          </div>
        </Router>
    )
  }
}
