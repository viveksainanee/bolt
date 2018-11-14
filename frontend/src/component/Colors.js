import React, { Component } from 'react';
import './Colors.css';

class Colors extends Component {
  render() {
    const colors = [
      'rgb(237,249,247)',
      'rgb(240,214,79)',
      'rgb(191,136,216)',
      'rgb(79,74,200)',
      'rgb(55,45,132)',
      'rgb(30,21,76)'
    ];
    return (
      <div className="Colors-cont">
        {colors.map(c => {
          return (
            <div className="Colors-swatch" style={{ backgroundColor: c }}>
              {c}
            </div>
          );
        })}
      </div>
    );
  }
}

export default Colors;
