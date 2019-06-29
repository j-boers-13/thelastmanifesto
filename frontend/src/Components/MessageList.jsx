import React, {Component} from 'react';

export default class MessageList extends Component {
  render() {
    return(
      <ul className="message-list">
        {this.props.messages.map(message => {
          return (
            <li key={message.id}>
              <div>
                {message.senderId}<br />
                {message.text}
              </div>
            </li>
          )
        })}
      </ul>
    )
  }
}
