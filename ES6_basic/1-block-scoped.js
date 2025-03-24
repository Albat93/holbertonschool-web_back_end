export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const task = true;  // cette variable est différente de celle du haut
    const task2 = false;
  }

  return [task, task2];
}
