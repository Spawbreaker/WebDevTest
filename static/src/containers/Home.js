import React, { Component } from "react";
import "./Home.css"

export default class Home extends Component {
    render() {
        return (
            <div className="Home">
                <div className="lander">
                    <h1>Bearsite</h1>
                    <p>A simple test app with React, Flask, and MongoDB</p>
                </div>
            </div>);
    }
}