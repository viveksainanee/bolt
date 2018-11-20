import React, { Component } from 'react';
import './Workspace.css';
import Topbar from './Topbar';
import TaskColumn from './TaskColumn';

class Workspace extends Component {
  render() {
    return (
      <div className="Workspace">
        <Topbar />
        <TaskColumn type="To Do" />
        {/* <TaskColumn type="In Progress" />
        <TaskColumn type="Complete" /> */}
      </div>
    );
  }
}

export default Workspace;
