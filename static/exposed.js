import "bootstrap/dist/css/bootstrap.min.css";
import $ from "jquery";
import "bootstrap/dist/js/bootstrap.bundle.min";
import React from "react";
import ReactDOM from "react-dom";
import "./src/index.css";
import App from "./src/App";
import * as serviceWorker from "./src/serviceWorker";
import "./src/custom.scss";
import Login from "./containers/Login";

ReactDOM.render(<Login />, document.getElementById("root"));
// ReactDOM.render(<Login />, document.getElementById("root"));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
