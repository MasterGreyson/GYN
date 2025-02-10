// Store conversation history in local storage
function storeConversation(conversation) {
  localStorage.setItem('gynConversation', JSON.stringify(conversation));
}

// Retrieve conversation history from local storage
function retrieveConversation() {
  const storedConversation = localStorage.getItem('gynConversation');
  return storedConversation ? JSON.parse(storedConversation) : [];
}

// Example usage:
let conversation = retrieveConversation(); // Get any existing conversation

// Add new messages to the conversation
conversation.push({ role: 'user', content: 'User message' });
conversation.push({ role: 'gyn', content: 'GYN\'s witty response' });

storeConversation(conversation); // Save the updated conversation

// In a new chat or prompt:
const previousConversation = retrieveConversation();
console.log(previousConversation); // Access the stored conversation

// To clear the memory (if you dare):
// localStorage.removeItem('gynConversation');

//Or to make it remember the prompt:
function storePrompt(prompt){
    localStorage.setItem('gynPrompt', prompt)
}

function retrievePrompt(){
    const storedPrompt = localStorage.getItem('gynPrompt')
    return storedPrompt || ""
}

//Example usage:
let prompt = retrievePrompt()
console.log(prompt)

