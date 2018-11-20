import React, { Component } from 'react';
import AddTaskForm from './AddTaskForm';
import './TaskColumn.css';

class TaskColumn extends Component {
  constructor(props) {
    super(props);
    this.state = {
      //TODO: connect to redux
      tasks: []
    };
    this.addTaskToColumn = this.addTaskToColumn.bind(this);
  }

  addTaskToColumn(task) {
    console.log(task);
    this.setState({
      tasks: [...this.state.tasks, task]
    });
  }

  render() {
    let tasks = this.state.tasks;
    return (
      <div className="TaskColumn">
        <h2> {this.props.type}</h2>
        <div>
          {tasks}
          <AddTaskForm addTaskToColumn={this.addTaskToColumn} />
        </div>
      </div>
    );
  }
}

export default TaskColumn;
