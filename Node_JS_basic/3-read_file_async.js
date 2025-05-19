const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');

      if (lines.length <= 1) {
        process.stdout.write('Number of students: 0\n');
        resolve();
        return;
      }

      const students = lines.slice(1);
      const fields = {};

      for (const student of students) {
        const values = student.split(',').map((x) => x.trim());
        if (values.length < 4) continue;
        const [firstName, , , field] = values;

        if (!fields[field]) fields[field] = [];
        fields[field].push(firstName);
      }

      process.stdout.write(`Number of students: ${students.length}\n`);

      for (const field of Object.keys(fields)) {
        const list = fields[field];
        process.stdout.write(
          `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}\n`
        );
      }

      resolve();
    });
  });
}

module.exports = countStudents;
