import React, { Component } from 'react';
import Sidebar from './Sidebar';
import Workspace from './Workspace';
import './Dashboard';

class Dashboard extends Component {
  render() {
    // Temporarily hardcoding to only show dashboard
    return (
      <div className="container-fluid row">
        <Sidebar />
        <Workspace />
      </div>
    );
    // return <div>{this.props.currUser ? <Dashboard /> : <Portal />}</div>;
  }
}

export default Dashboard;
