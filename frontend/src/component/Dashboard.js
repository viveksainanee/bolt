import React, { Component } from 'react';
import Sidebar from './Sidebar';
import Workspace from './Workspace';
import './Dashboard.css';
import Topbar from './Topbar';

class Dashboard extends Component {
  render() {
    return (
      <div className="container-fluid ">
        <div className="Dashboard">
          <Topbar />
        </div>
        <div className="row">
          <Sidebar />
        </div>
        <div>
          <Workspace />
        </div>
      </div>
    );
  }
}

export default Dashboard;
