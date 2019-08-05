import React, { Component } from "react";
import "./DhuumTogether.css"
import { Button, ProgressBar, FormGroup, FormControl, FormLabel } from "react-bootstrap";
import { withRouter } from 'react-router-dom';
import queryString from "query-string";



export default class DhuumTogether extends Component {
    constructor(props) {
        super(props);
        this.state = {
            id: '',
            running: false,
            joined: false,
            failed: false, 
            time: 0
        };
    }

    getTime() {
        const mins = Math.floor((600 - this.state.time) / 60);
        const secs = (600 - this.state.time) % 60;
        return `${mins > 9 ? mins : '0' + mins}:${secs > 9 ? secs : '0' + secs}`
    }

    handleChange = event => {
        this.setState({[event.target.id]: event.target.value});
    };

    handleStartBtn = (event) => {
        this.changeStatus();
    }

    toggleDhuumStopwatch(toState) {
        var _this = this;
        _this.setState({ running: toState });
        if (this.state.running) {
            this.timerRun = setInterval(function () {
                _this.setState({ time: (_this.state.time + 1) });
            }, 1000)
        }
        else {
            _this.setState({ time: 0 });
            clearInterval(this.timerRun);
        }
    }

    validateRoomName() {
        return this.state.id.length > 3;
    }

    startPollingServer(){
        console.log("Starting timer to query the server to start " + this.state.joined)
        var _this = this;        
        _this.listeningForState = setInterval(function () {
            const id = _this.state.id;                
            fetch("http://127.0.0.1:5000/dhuum/" + id)
                .then(response => response.json())
                .then(response => {                    
                    // console.log(typeof response.running)
                    var rsp = response.running == "True";
                    if (_this.state.running != rsp) {                    
                        _this.toggleDhuumStopwatch(rsp);    
                    }                                                                                                         
                });     
        }, 1000);
        console.log("Started the timer!");    
    }

    changeStatus() {
        console.log('Requesting to flip the status on the server');
        const _id = this.state.id;
        const _running = !this.state.running;
        this.setState({ isLoading: true });
        fetch("http://127.0.0.1:5000/dhuum/update/", {
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            method: "POST",
            body: JSON.stringify({
                id: _id,
                running: _running
            })
        }).then(response => response.json()).then(
            response => {
                this.setState({ isLoading: false });            
            }
        );
    }

    handleGetRoom = (event) =>{        
        console.log("Starting a room request for the id " + this.state.id)        
        const id = this.state.id;
        this.setState({ isLoading: true });
        fetch("http://127.0.0.1:5000/dhuum/" + id)
        .then(response => response.json())
        .then(response => {
            console.log("The response code is successful? " + response.statusCode)
            console.log("Is it equal to 200?" + (response.statusCode == 200))
            this.setState({
                joined: response.statusCode==200, 
                failed: response.statusCode==500,                                            
                isLoading:false
            })                         
            this.startPollingServer();               
        });
    }

    
    


    render() {
        return (
            <div className="DhuumTogether">
                <div className="container">
                    <h1>Dhuum Together</h1>
                    
                    <p>No more hassle</p>
                    <div className="joinContainer">
                        <form>
                            <FormGroup controlId="id" bsSize="Large">
                                <FormLabel>Room name</FormLabel>
                                <FormControl
                                    autoFocus
                                    type="text"
                                    value={this.state.id}
                                    onChange={this.handleChange}
                                    className="idTextbox"
                                    placeholder="Type the name of the room you want to join or make!"
                                    disabled={this.state.joined}
                            />
                                <Button block
                                    className={this.state.joined?"hidden":""}
                                    variant="primary"
                                    size="lg"
                                    onClick={!this.isLoading ? this.handleGetRoom : null}
                                    disabled={!this.validateRoomName()}>                                    
                                    {!this.isLoading ? "Dhuum's gaze falls on me!" : "Protect the reapers while I channel your room!"}</Button>
                            </FormGroup>
                        </form>
                    </div>
                    <div className={this.state.joined ? "timerContainer" : "hidden"} >
                        <ProgressBar
                            now={606 - this.state.time}
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