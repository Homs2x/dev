document.addEventListener("DOMContentLoaded", function() {
    // Get the modal and button
    const modal = document.getElementById("eventModal");
    const button = document.getElementById("open-event-modal-button");
    const closeButton = document.getElementById("close-modal");
  
    // When the button is clicked, display the modal
    button.addEventListener("click", function() {
      modal.style.display = "block";
    });
  
    // When the close button is clicked, hide the modal
    closeButton.addEventListener("click", function() {
      modal.style.display = "none";
    });
  
    // When the user clicks outside the modal, hide it
    window.addEventListener("click", function(event) {
      if (event.target === modal) {
        modal.style.display = "none";
      }
    });
  
    // Handle form submission here, e.g., send data to the server
    const eventForm = document.getElementById("event-creation-form");
    eventForm.addEventListener("submit", function(event) {
      event.preventDefault();
      // Add code to process the form data and send it to the server
      // For a static example, you can just hide the modal
      modal.style.display = "none";
    });
  });

  // Sample event data (replace with actual data)
const eventsData = [
    {
      title: "Event 1",
      date: "2023-10-31",
      duration: "2 hours",
      description: "Description for Event 1",
      author: "Author 1",
    },
    {
      title: "Event 2",
      date: "2023-11-15",
      duration: "3 hours",
      description: "Description for Event 2",
      author: "Author 2",
    },
  ];
  
  // Function to create an event listing
  function createEventListing(event) {
    const eventListing = document.createElement("div");
    eventListing.classList.add("event");
    eventListing.innerHTML = `
      <h3>${event.title}</h3>
      <p>Date: ${event.date}</p>
      <p>Duration: ${event.duration}</p>
      <p>Description: ${event.description}</p>
      <p>Author: ${event.author}</p>
    `;
    return eventListing;
  }
  
  // Function to display events
  function displayEvents() {
    const eventListContainer = document.getElementById("event-list-container");
  
    // Clear existing content
    eventListContainer.innerHTML = "";
  
    // Create and append event listings
    eventsData.forEach((event) => {
      const eventListing = createEventListing(event);
      eventListContainer.appendChild(eventListing);
    });
  }
  
  // Call the function to display events
  displayEvents();
  