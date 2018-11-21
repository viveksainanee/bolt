import React, { Component } from 'react';
import { NavLink } from 'react-router-dom';

import './Topbar.scss';

class Topbar extends Component {
  render() {
    return (
      <div className="Topbar fixed-top">
        <div id="TopBar-tasks">
          <span id="TopBar-teamTasks">
            <NavLink to="/teamtasks">team tasks</NavLink>
          </span>
          <span id="TopBar-myTasks">
            <NavLink to="/mytasks">my tasks</NavLink>
          </span>
        </div>
        <span id="TopBar-logOut">
          <NavLink to="/logout">log out</NavLink>
        </span>
      </div>
    );
  }
}

export default Topbar;
