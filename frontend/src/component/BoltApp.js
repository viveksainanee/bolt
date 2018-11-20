import React, { Component } from 'react';
import Dashboard from './Dashboard';
import Portal from './Portal';
import './BoltApp.css';

class BoltApp extends Component {
  render() {
    // Temporarily hardcoding to only show dashboard
    return (
      <div id="BoltApp" className="row">
        <Dashboard />
      </div>
    );
    // return <div>{this.props.currUser ? <Dashboard /> : <Portal />}</div>;
  }
}

export default BoltApp;
