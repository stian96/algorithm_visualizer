// Function to reset background color of HTML elements
function resetBackgroundColors(elements) {
    for (let item of elements) {
        item.style.backgroundColor = '';
    }
}

// Sleep function to delay execution
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Function to add an event listener to a specified element
// The listener sends a POST request to the specified url when the element is clicked
// and changes the background color of the elements in a list based on the response
function addEventListenerForSearch(elementId, url, onStepCallback) 
{
    document.getElementById(elementId).addEventListener('click', async function() 
    {
        clearCallStack();
        let element = document.getElementById('element').value;
        isInputFieldEmpty(element)

        console.log(`Element to search for: ${element}`);
        let steps = await getSearchResult(url, element);
        let listItems = document.querySelectorAll('.flex-item');

        for (let step of steps) {
            let listItem = Array.from(listItems).find(item => item.textContent === step.value.toString());

            if (listItem) {
                listItem.style.backgroundColor = step.found ? 'green' : 'rgb(248, 110, 110)';
            }
            onStepCallback(step)
            await sleep(1000);
        }
        await sleep(2000)
        resetBackgroundColors(listItems)
    });
}

// Function to send a POST request to the specified url with the element to search for
// and return the steps to find the element as a promise
async function getSearchResult(url, element) {
    try {
        let response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({element: element})
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        let data = await response.json();
        if (!data.hasOwnProperty('steps')) {
            throw new Error("Missing 'steps' key in response.");
        }
        return data['steps'];
    } 
    catch(error) {
        console.log('A problem occurred while fetching the search steps:', error);
    }
}

function updateCallStack(element) {
    let callStack = document.getElementById('call-stack');
    let stackItem = document.createElement('li');
    stackItem.className = 'stack-item';
    stackItem.textContent = element.value;
    callStack.appendChild(stackItem);
}

function clearCallStack() {
    let callStack = document.getElementById('call-stack');
    while (callStack.firstChild) {
        callStack.removeChild(callStack.firstChild);
    }
}

function isInputFieldEmpty(element) {
    if (element === '') {
        alert('Please enter a value to search for in the input field.')
        return;
    }
}


// Add event listeners for different search algorithms.
addEventListenerForSearch('linear-search', '/linear-search', function() {});
addEventListenerForSearch('binary-search', '/binary-search', function() {});
addEventListenerForSearch('recursive-search', '/recursive-search', updateCallStack);