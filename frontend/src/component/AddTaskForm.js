import React, { Component } from 'react';

class AddTaskForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      title: ''
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(evt) {
    this.setState({
      [evt.target.name]: evt.target.value
    });
  }

  handleSubmit(evt) {
    evt.preventDefault();
    //TODO: redux
    this.props.addTaskToColumn(this.state);
    this.setState({
      title: ''
    });
  }

  render() {
    return (
      <form className="AddTaskForm" onSubmit={this.handleSubmit}>
        <input
          name="title"
          value={this.state.title}
          onChange={this.handleChange}
          placeholder="add task"
        />
      </form>
    );
  }
}

export default AddTaskForm;
