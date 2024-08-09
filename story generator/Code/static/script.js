document.getElementById('storyForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const prompt = document.getElementById('prompt').value;

    console.log(`Sending prompt: ${prompt}`);  // Debug print

    const response = await fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt })
    });

    const data = await response.json();
    console.log(data);  // Debug print
    const storyContainer = document.getElementById('storyContainer');
    const storyDiv = document.getElementById('story');
    if (data.story) {
        storyDiv.textContent = data.story;
        storyContainer.style.display = 'block';
    } else {
        storyDiv.textContent = 'Error generating story';
        storyContainer.style.display = 'block';
    }
});
