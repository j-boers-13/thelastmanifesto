import React, { Component } from 'react'
import { Switch, Route } from "react-router-dom"
import Homepage from './Homepage'

export default class Container extends Component {
  render(){
    return(
        <Switch>
          <Route exact path="/" component={Homepage} />
          <Route path="/about" component={Homepage} />
          <Route path="/social" component={Homepage} />
          <Route path="/news" component={Homepage} />
          <Route path="/thewall" component={Homepage} />
        </Switch>
    )
  }
}
