import React, { Component } from "react";
import { Link } from "react-router-dom";
import { Nav, Navbar } from "react-bootstrap";
import "./App.css";
// import Home from "./containers/Home";
import Routes from "./Routes";

class App extends Component {
  render() {
    return (
      <div className="App container" >
        <Navbar fluid collapseOnSelect bg="secondary">
          <div class="navbar-header">
            <Navbar.Brand>
              <Link to="/">BearSite</Link>
            </Navbar.Brand>
            <Navbar.Toggle />
          </div>
          <Nav className="mr-auto">
            <Nav.Link href="/login">Login</Nav.Link>
            <Nav.Link href="/dhuum">Dhuum</Nav.Link>
          </Nav>
        </Navbar>
        <Routes />
      </div>
    );
  }
}

export default App;
