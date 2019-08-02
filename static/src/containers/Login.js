import React, { Component } from "react";
import { Button, FormGroup, FormControl, FormLabel } from "react-bootstrap";
import "./Login.css";
import banner from "../img/red-panda.jpg"

export default class Login extends Component {
  constructor(props) {
    super(props);

    this.state = {
      // user: {
      email: "",
      password: ""
      // },
    };
  }

  validateForm() {
    return this.state.email.length > 0 && this.state.password.length > 0;
  }

  handleChange = event => {
    this.setState({
      [event.target.id]: event.target.value
    });
  };

  handleSubmit = (event) => {
    // event.preventDefault();
    const em = this.state.email;
    const pw = this.state.password;

    // this.state.response = pw;
    this.setState({ isLoading: true });
    fetch("http://127.0.0.1:5000/login/", {
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json"
      },
      method: "POST",
      body: JSON.stringify({
        name: em,
        password: pw
      })
    })
      .then(response => response.json())
      .then(response => {
        this.setState({
          result: response.result,
          isLoading: false
        });

      })
  };

  render() {
    return (
      <div className="Login">
        <div className="Banner">
          <img src={banner} alt="Banner" />
          <h1>Bears</h1>
          {/* . */}
        </div>
        <form>
          <FormGroup controlId="email" bsSize="Large">
            <FormLabel>Email</FormLabel>
            <FormControl
              autoFocus
              type="email"
              value={this.state.email}
              onChange={this.handleChange}
            />
          </FormGroup>
          <FormGroup controlId="password" bsSize="Large">
            <FormLabel>Password</FormLabel>
            <FormControl
              value={this.state.password}
              onChange={this.handleChange}
              type="password"
            />
          </FormGroup>
          <Button
            block
            // className="LoginBtn"
            variant="outline-primary"
            bsSize="Large"
            disabled={!this.validateForm()}
            // type="submit"
            onClick={!this.state.isLoading ? this.handleSubmit : null}
          >
            {this.state.isLoading ? 'Logging in' : 'Login'}
          </Button>
        </form>
        <div className="panel panel-default">
          <div className="panel-body">{this.state.result}</div>
        </div>
      </div>
    );
  }
}
