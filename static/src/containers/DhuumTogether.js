import React, { Component } from "react";
import "./DhuumTogether.css"
import { Button, ProgressBar } from "react-bootstrap";



export default class DhuumTogether extends Component {

    constructor(props) {
        super(props);

        this.state = {
            time: 0,
            running: false
        };
    }

    getTime() {
        const mins = Math.floor((600 - this.state.time) / 60);
        const secs = (600 - this.state.time) % 60;
        return `${mins > 9 ? mins : '0' + mins}:${secs > 9 ? secs : '0' + secs}`
    }

    handleStartBtn = (event) => {
        var _this = this;
        this.setState({ running: !this.state.running });
        if (!this.state.running) {
            this.timerRun = setInterval(function () {
                _this.setState({ time: (_this.state.time + 1) });
            }, 1000)
        }
        else {
            clearInterval(this.timerRun);
        }
    }


    render() {
        return (
            <div className="DhuumTogether">
                <div className="container">
                    <h1>Dhuum Together</h1>
                    <p>No more hassle</p>
                    <div className="timerContainer">
                        <ProgressBar
                            now={600 - this.state.time}
                            label={this.getTime()}
                            max="600"
                            className="timerBar"
                            animated={this.state.running} />
                        <Button block
                            variant="outline-primary"
                            size="lg"
                            onClick={this.handleStartBtn}>
                            {this.state.running ? 'Stop' : 'Start'}</Button>
                    </div>
                </div>
            </div>);
    }
}