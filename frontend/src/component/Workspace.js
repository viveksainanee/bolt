import React, { Component } from 'react';
import './Workspace.css';
// import Topbar from './Topbar';
import TaskColumn from './TaskColumn';

class Workspace extends Component {
  render() {
    return (
      <div className="Workspace">
        <div className="TaskColumnRow">
          <TaskColumn type="To Do" />
          <TaskColumn type="In Progress" />
          <TaskColumn type="Complete" />
        </div>
      </div>
    );
  }
}

export default Workspace;
