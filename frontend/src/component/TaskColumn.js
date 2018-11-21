import React, { Component } from 'react';
import AddTaskForm from './AddTaskForm';
import Task from './Task';
import './TaskColumn.scss';

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
    console.log(this.state);
    this.setState(st => ({
      tasks: [...st.tasks, task]
    }));
  }

  render() {
    let titles = this.state.tasks.map(task => <Task {...task} />);

    return (
      <div className="TaskColumn">
        <div className="TaskColumn-type">{this.props.type}</div>
        {titles}
        <div>
          <AddTaskForm addTaskToColumn={this.addTaskToColumn} />
        </div>
      </div>
    );
  }
}

export default TaskColumn;
