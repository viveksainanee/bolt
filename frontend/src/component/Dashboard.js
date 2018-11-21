import React, { Component } from 'react';
import Sidebar from './Sidebar';
import Workspace from './Workspace';
import './Dashboard.css';

class Dashboard extends Component {
  render() {
    return (
      <div className="container-fluid row Dashboard">
        <Sidebar />
        <Workspace />
      </div>
    );
    // return <div>{this.props.currUser ? <Dashboard /> : <Portal />}</div>;
  }
}

export default Dashboard;
