import React, { PureComponent } from 'react'
import { BrowserRouter as Router, Route, Link} from "react-router-dom"

import './Styles/Navbar.css'

class Navbar extends PureComponent {
  render () {
    return (
        <nav className="navbar navbar-inverse">
          <div className="navbar-head">
              <button type="button" className="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                  <span className="icon-bar"></span>
                  <span className="icon-bar"></span>
                  <span className="icon-bar"></span>
              </button>
              <Link className="navbar-brand" to="/">the last manifesto</Link>
          </div>
          <div className="collapse navbar-collapse" id="myNavbar">
              <ul className="nav navbar-nav">
                  <li><Link to="/events">Events</Link></li>
                  <li><Link to="/social">Social</Link></li>
                  <li><Link to="/news">News</Link></li>
                  <li><Link to="/events">TheWall</Link></li>
              </ul>
              <ul class="nav navbar-nav navbar-right">
                  <li><Link to="/signup"><span className="glyphicon glyphicon-user"></span> Sign Up</Link></li>
                  <li><Link to="/login"><span className="glyphicon glyphicon-log-in"></span> Login</Link></li>
              </ul>
          </div>
        </nav>
    )
  }
}

export default Navbar;
