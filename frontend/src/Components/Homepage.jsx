import React, { Component, PureComponent } from 'react'
import { Switch, Route } from "react-router-dom"

import './Styles/Landing.css'
import './Styles/About.css'

import Landing from './Landing'
import About from './About'

export default class Homepage extends PureComponent {
  render(){
    return(
      <Switch>
        <Route exact path='/' component={Landing} />
        <Route path='/about' component={About} />
      </Switch>
    )
  }
}
