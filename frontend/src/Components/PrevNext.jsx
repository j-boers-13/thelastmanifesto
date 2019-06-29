import React, { Component } from 'react'

import './Styles/Button.css'

export default class Container extends Component {
  render(){
      return(
      <div className ="prevNext">
      <button id="prevnext" onClick={this.props.prevClick}>
        Previous
      </button>
      <button id="prevnext" onClick={this.props.nextClick}>
        Next
      </button>
    </div>
    )
  }
}
