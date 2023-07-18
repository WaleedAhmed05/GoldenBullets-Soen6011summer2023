//// dashboard.js
//document.getElementById('create-job-form').addEventListener('submit', function (event) {
//  event.preventDefault(); // Prevent form submission
//
//  // Get form data
//  const title = document.getElementById('title').value;
//  const description = document.getElementById('description').value;
//  const requirements = document.getElementById('requirements').value;
//
//  // Create job posting object
//  const jobPosting = {
//    title: title,
//    description: description,
//    requirements: requirements
//  };
//
//  // Send POST request to Flask server
//  fetch('/create_job', {
//    method: 'POST',
//    headers: {
//      'Content-Type': 'application/json'
//    },
//    body: JSON.stringify(jobPosting)
//  })
//  .then(response => response.json())
//  .then(data => {
//    // Handle server response if needed
//    console.log(data);
//  })
//  .catch(error => {
//    // Handle error if any
//    console.error(error);
//  });



      $(function() {
      // Example list of job title options
      const jobTitleOptions = ['Accounts associate','Call centre associate','Call centre supervisor',
      'Client manager','Complaints manager','Customer relations manager','Customer service agent','Customer service representative',
      'Relationship manager','Sales adviser','Assistant professor','Childcare assistant','English teacher',
      'Lecturer','Piano teacher','Private tutor','Professor','Agricultural labourer','Beekeeper',
      'Ecologist','Farmer','Fisher','Plant scientist','Meatpacker','Horticulturist','Food scientist','Food inspector',
      'Animal control officer','Animal geneticist','Zoologist','Wildlife biologist','Veterinarian',
      'Pet walker','Dog groomer','Cat sitter','Breeder','Animal nutritionist','Accountant',
      'Business development assistant','Business manager','Customer service associate','Financial advisor',
      'Managing director','Office clerk','Office manager','Project manager','Retail manager','Barber','Beautician',
      'Beauty therapist','Fashion designer','Hairdresser','Hair stylist','Nail technician','Salon assistant',
      'Salon manager','Skin care specialist','Artist','Copywriter','Costume designer','Film director','Journalist',
      'Music producer','Musician','Opera singer','Set designer','Writer','School administrator','School custodian','Teacher',
      'Chemical engineer','Civil engineer','Environmental engineer','Marine engineer','Mechanical engineer','Petroleum engineer',
      'Product designer','Product engineer','Service engineer','Technical engineer','Auditor','Banker','Budget analyst',
      'Credit analyst','Financial advisor','Financial director','Financial manager','Financial officer','Investment banker',
      'Loan agent','Care aid','Care worker','Dentist','Doctor','Medical assistant','Nurse','Nursing assistant','Optician',
      'Physician','Physical therapist','Chef','Cleaner','Events organizer','Hotel clerk','Hotel manager','Housekeeper',
      'Meeting planner','Tour guide','Travel agent','Waiter','Administrative assistant','Benefits manager',
      'Employee relations manager','Executive recruiter','Human resources assistant','Human resources director',
      'Human resources manager','Labour relations specialist','Recruiting agent','Staffing assistant','Computer programmer',
      'Information security analyst','IT manager','Programmer','Service technician','Software developer','Software tester',
      'UI developer','Web administrator','Web analyst','Business director','Chief executive','Chief operations officer',
      'Director','Executive','Head of department','Managing director','Supervisor','Team leader','Team manager',
      'Accounts executive','Content manager','Creative director','Marketer','Marketing assistant','Marketing coordinator',
      'Marketing director','Marketing manager','Social media assistant','Social media manager','Distributions manager',
      'Logistics coordinator','Logistics officer','Operations assistant','Operations manager','Product coordinator',
      'Quality assurance officer','Quality control manager','Supply chain specialist','Warehouse supervisor',
      'Account coordinator','Cashier','Clerk','Insurance agent','Retail assistant','Sales associate','Sales director',
      'Sales representative','Store person','Telemarketer'];

      // Initialize autocomplete on the job title input field
      $("#title").autocomplete({
        source: jobTitleOptions
      });


      // Track selected shift and schedule options
      let selectedShiftSchedule = [];

      // Add shift and schedule option
      $(".add-shift-schedule").click(function() {
        const shiftScheduleSelect = $("#shift-schedule-select");
        const shiftSchedule = shiftScheduleSelect.val().trim();

        if (selectedShiftSchedule.includes(shiftSchedule)){
            alert("Option already selected!");
            return;
          }

        if (shiftSchedule !== "" && !selectedShiftSchedule.includes(shiftSchedule)) {
          selectedShiftSchedule.push(shiftSchedule);
          $(".selected-shift-schedule").append(`<span class="shift-schedule-label">${shiftSchedule}<button class="remove-shift-schedule">x</button></span>`);
          shiftScheduleSelect.val("");
<!--          shiftScheduleSelect.find(`option[value="${shiftSchedule}"]`).prop("disabled", true);-->
        }
      });

      // Remove shift and schedule option
      $(document).on("click", ".remove-shift-schedule", function() {
        const shiftScheduleLabel = $(this).parent();
        const shiftSchedule = shiftScheduleLabel.text().trim();

        const index = selectedShiftSchedule.indexOf(shiftSchedule);
        if (index > -1) {
          selectedShiftSchedule.splice(index, 1);
        }

        shiftScheduleLabel.remove();
<!--        $("#shift-schedule-select").find(`option[value="${shiftSchedule}"]`).prop("disabled", false);-->
      });

      // Enable previously removed options
      $("#shift-schedule-select").change(function() {
        const selectedOption = $(this).val();
        const optionElement = $(this).find(`option[value="${selectedOption}"]`);
        optionElement.disabled = false;
      });


      // Track selected shift and schedule options
      let selectedLanguage = [];

      // Add shift and schedule option
      $(".add-language").click(function() {
        const languageSelect = $("#language-select");
        const language = languageSelect.val().trim();

        if (selectedLanguage.includes(language)){
            alert("Option already selected!");
            return;
          }

        if (language !== "" && !selectedLanguage.includes(language)) {
          selectedLanguage.push(language);
          $(".selected-language").append(`<span class="language-label">${language}<button class="remove-language">x</button></span>`);
          languageSelect.val("");
<!--          languageSelect.find(`option[value="${language}"]`).prop("disabled", true);-->
        }
      });

      // Remove shift and schedule option
      $(document).on("click", ".remove-language", function() {
        const languageLabel = $(this).parent();
        const language = languageLabel.text().trim();

        const index = selectedLanguage.indexOf(language);
        if (index > -1) {
          selectedLanguage.splice(index, 1);
        }

        languageLabel.remove();
<!--        $("#language-select").find(`option[value="${language}"]`).prop("disabled", false);-->
      });

      // Enable previously removed options
      $("#language-select").change(function() {
        const selectedOption = $(this).val();
        const optElement = $(this).find(`option[value="${selectedOption}"]`);
        optElement.disabled = false;
      });
    });

//});