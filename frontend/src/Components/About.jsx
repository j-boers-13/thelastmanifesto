import React, { Component, PureComponent } from 'react'
import { Route, Link, Redirect } from 'react-router-dom'

import PrevNext from './PrevNext'


export default class About extends PureComponent{

  constructor(props){
    super(props)
    this.state =  { page : 1, pages: 3 }
    this.nextClick = this.nextClick.bind(this)
    this.prevClick = this.prevClick.bind(this)
  }

  nextClick(){
    if(this.state.page === 3){
      this.setState({
        page: 1
      })
    }
    else {
      this.setState({
        page: this.state.page + 1
      })
    }
  }

  prevClick(){
    if(this.state.page === 1){
      this.setState({
        page: 3
      })
    }
    else{
      this.setState({
        page: (this.state.page - 1)
      })
    }
  }

  render(){
    if(this.state.page == 1){
      return(
      <div id="about">
        <div id ="aboutimg">
            <div id="abouttitle">
                Climate change.
            </div>
          </div>
        <div id ="abouttxt">
          Despite urgent warnings from scientific communities, climate change is still a low priority for many citizens of the world.
        <br/><br/>
          Large corporations and governments are allowing the degradation and pollution of our environment, which leads to endangering our future, as well as that of the many species that make up earth's great biodiversity.

        </div>
      <PrevNext prevClick = {this.prevClick} nextClick = {this.nextClick} />
      </div>
      )
    }
    if(this.state.page == 2){
      return(
      <div id="about2">
        <div id="aboutimg2">
          <div id="abouttitle2">
              By students
              for students.
          </div>
        </div>
        <div id ="abouttxt2">
          The last manifesto serves as a platform for taking on the fight against climate change. <br /> <br />
          We call upon the younger generations and the future generations to help us spread awareness, inspire people to take action and expose the ones that are knowingly destroying our environment.
        </div>
        <PrevNext prevClick = {this.prevClick} nextClick = {this.nextClick} />
      </div>
      )
    }
    if(this.state.page == 3){
      return(
      <div id="about3">
        <div id="aboutimg3">
          <div id="abouttitle3">
            Join the fight!
          </div>
        </div>
        <div id ="abouttxt3">
          Help us create the last manifesto. Together we can do much more than just on our own.<br /><br />
          At <span id = "tlm">the last manifesto</span> you can create and attend events, set up a social profile and discuss several topics. We also aim to encourage discussion on the latest climate change related news in our news section. The wall serves as a wall of shame for big companies that destroy the earth.<br />


        </div>
        <PrevNext prevClick = {this.prevClick} nextClick = {this.nextClick} />
      </div>
      )
    }
  }
}
