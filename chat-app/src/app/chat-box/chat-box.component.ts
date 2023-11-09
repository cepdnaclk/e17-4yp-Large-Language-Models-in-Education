import { Component } from '@angular/core';
import {ChatServiceService} from "../chat-service.service";

@Component({
  selector: 'app-chat-box',
  templateUrl: './chat-box.component.html',
  styleUrls: ['./chat-box.component.css']
})
export class ChatBoxComponent {
  messages: { content: string; isUser: boolean }[] = [];
  newMessage: string = '';

  constructor(private chatService: ChatServiceService) {
  }
  sendMessage() {
    if (this.newMessage.trim() !== '') {
      this.messages.push({ content: this.newMessage, isUser: true });

      this.chatService.getAnswer(this.newMessage)
        .subscribe((resp)=>{
          console.log(resp);
          this.messages.push({ content: resp, isUser: false });
          // You can implement logic here to handle bot responses or other functionalities.
          this.newMessage = ''; // Clear the input field after sending the message.


        })

      // // You can implement logic here to handle bot responses or other functionalities.
      // this.newMessage = ''; // Clear the input field after sending the message.
    }
  }
}
