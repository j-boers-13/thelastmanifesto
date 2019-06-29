import React, { Component, PureComponent } from 'react'
import { Link, Switch, Route } from "react-router-dom"

export default class Landing extends PureComponent {
  render(){
    return(
    <div id="home-bg">
      <div id="landing-text">
        <h1 id="intro">
          the last manifesto
        </h1>
        <h2 id="intro2">
          A collective last effort to save mankind.
        </h2>
        <h3 id="intro3">
          <Link to ="/about">Learn more.</Link>
        </h3>
        <h3 id="intro3">
          <a href="#join">Log in.</a>
        </h3>
        <h3 id="intro3">

          <a href="#join">Who are we?</a>
        </h3>
      </div>
    </div>
    )
  }
}
