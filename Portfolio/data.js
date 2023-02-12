var projects = [
  {
    title: "Project 1",
    description: "A description of Project 1 goes here.",
    link: "#"
  },
  {
    title: "Project 2",
    description: "A description of Project 2 goes here.",
    link: "#"
  },
  // Add more objects for additional projects
];

function displayProjects() {
  var projectContainer = document.querySelector(".project-container");
  projectContainer.innerHTML = "";

  for (var i = 0; i < projects.length; i++) {
    var project = projects[i];

    var projectDiv = document.createElement("div");
    projectDiv.classList.add("project");

    var title = document.createElement("h3");
    title.innerText = project.title;
    projectDiv.appendChild(title);

    var description = document.createElement("p");
    description.innerText = project.description;
    projectDiv.appendChild(description);

    var link = document.createElement("a");
    link.innerText = "See Project";
    link.href = project.link;
    projectDiv.appendChild(link);

    projectContainer.appendChild(projectDiv);
  }
}


window.onload = displayProjects;
