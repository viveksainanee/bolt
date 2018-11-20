import React, { Component } from 'react';
import Dashboard from './Dashboard';
import Portal from './Portal';

class BoltApp extends Component {
  render() {
    return <div>{this.props.currUser ? <Dashboard /> : <Portal />}</div>;
  }
}

export default BoltApp;
