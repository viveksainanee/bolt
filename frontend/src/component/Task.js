import React, { Component } from 'react';
import './Task.css';

class Task extends Component {
  render() {
    return (
      <div className="Task">
        <h3> {this.props.title}</h3>
      </div>
    );
  }
}

export default Task;
