const courseOptions = {
    'BE Computer': {
      'I': ['Course 1', 'Course 2', 'Course 3'],
      'II': ['Course 1', 'Course 2', 'Course 3'],
      'III': ['Course 1', 'Course 2', 'Course 3'],
      'IV': ['Course 1', 'Course 2', 'Course 3'],
      'V': ['Course 1', 'Course 2', 'Course 3'],
      'VI': ['Simulation and Modeling', 'Data Communication', 'Embedded System'],
      'VII': ['Course 1', 'Course 2', 'Course 3'],
      'VIII': ['Course 1', 'Course 2', 'Course 3']
    },
    'BE Civil': {
      'I': ['Course 1', 'Course 2', 'Course 3'],
      'II': ['Course 1', 'Course 2', 'Course 3'],
      'III': ['Course 1', 'Course 2', 'Course 3'],
      'IV': ['Course 1', 'Course 2', 'Course 3'],
      'V': ['Course 1', 'Course 2', 'Course 3'],
      'VI': ['Course 1', 'Course 2', 'Course 3'],
      'VII': ['Course 1', 'Course 2', 'Course 3'],
      'VIII': ['Course 1', 'Course 2', 'Course 3']
    },
    'BE Software': {
        'I': ['Course 1', 'Course 2', 'Course 3'],
        'II': ['Course 1', 'Course 2', 'Course 3'],
        'III': ['Course 1', 'Course 2', 'Course 3'],
        'IV': ['Course 1', 'Course 2', 'Course 3'],
        'V': ['Course 1', 'Course 2', 'Course 3'],
        'VI': ['Course 1', 'Course 2', 'Course 3'],
        'VII': ['Course 1', 'Course 2', 'Course 3'],
        'VIII': ['Course 1', 'Course 2', 'Course 3']
      },
    'BE IT': {
        'I': ['Course 1', 'Course 2', 'Course 3'],
        'II': ['Course 1', 'Course 2', 'Course 3'],
        'III': ['Course 1', 'Course 2', 'Course 3'],
        'IV': ['Course 1', 'Course 2', 'Course 3'],
        'V': ['Course 1', 'Course 2', 'Course 3'],
        'VI': ['Course 1', 'Course 2', 'Course 3'],
        'VII': ['Course 1', 'Course 2', 'Course 3'],
        'VIII': ['Course 1', 'Course 2', 'Course 3']
      },
    'BCA': {
        'I': ['Course 1', 'Course 2', 'Course 3'],
        'II': ['Course 1', 'Course 2', 'Course 3'],
        'III': ['Course 1', 'Course 2', 'Course 3'],
        'IV': ['Course 1', 'Course 2', 'Course 3'],
        'V': ['Course 1', 'Course 2', 'Course 3'],
        'VI': ['Course 1', 'Course 2', 'Course 3'],
        'VII': ['Course 1', 'Course 2', 'Course 3'],
        'VIII': ['Course 1', 'Course 2', 'Course 3']
      },
  };

  // Function to populate the course options based on the selected program and semester
  function populateCourseOptions() {
    const program = document.getElementById('program').value;
    const semester = document.getElementById('semester').value;
    const courseSelect = document.getElementById('course');

    // Clear existing options
    courseSelect.innerHTML = '<option value="">Select Course</option>';

    if (program && semester && courseOptions[program] && courseOptions[program][semester]) {
      const courses = courseOptions[program][semester];
      courses.forEach(course => {
        const option = document.createElement('option');
        option.text = course;
        option.value = course;
        courseSelect.appendChild(option);
      });
    }
  }
  document.getElementById('program').addEventListener('change', populateCourseOptions);
  document.getElementById('semester').addEventListener('change', populateCourseOptions);