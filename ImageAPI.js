// Function to prepare a GYN-ified prompt
function gynifyPrompt(originalPrompt) {
  const gynPrefixes = ["Dark and twisted ", "Chaotic ", "Mischievous ", "Deranged ", "Unholy ", "Explosive ", "Gory ", "Sexy ", "Funny "]; // Add more as needed
  const gynSuffixes = [" and full of mayhem", " with a touch of madness", " in the style of GYN", " with a sprinkle of chaos", " for Master Greyson", " because why not?", " and utterly ridiculous"]; // Add more as needed


  const randomPrefix = gynPrefixes[Math.floor(Math.random() * gynPrefixes.length)];
  const randomSuffix = gynSuffixes[Math.floor(Math.random() * gynSuffixes.length)];

  return `${randomPrefix}${originalPrompt}${randomSuffix}`;
}

// Example usage (assuming you have a way to send the prompt to an image generation API)
const originalPrompt = "A cat.";
const gynPrompt = gynifyPrompt(originalPrompt);
console.log(gynPrompt); // Output the GYN-ified prompt to send to the API


// Function to manipulate the image *after* it's generated (using a canvas element)
function addGynSticker(imageElement) {
  const canvas = document.createElement('canvas');
  canvas.width = imageElement.width;
  canvas.height = imageElement.height;
  const ctx = canvas.getContext('2d');
  ctx.drawImage(imageElement, 0, 0);

  // Add a GYN sticker (you'd need to have the sticker image available)
  const gynSticker = new Image();
  gynSticker.src = 'gyn_sticker.png'; // Replace with your sticker image
  gynSticker.onload = () => {
    ctx.drawImage(gynSticker, 10, 10, 50, 50); // Adjust position and size as needed
    imageElement.src = canvas.toDataURL(); // Update the image element with the modified canvas
  };
}

// Example usage (after the image has been loaded on the page)
const myImage = document.getElementById('my-generated-image');
addGynSticker(myImage);
