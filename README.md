# Algorithmic Complexity, Approximation and Randomized Algorithms

## Task 1. Comparing Randomized and Deterministic QuickSort

### Description

Implement both **randomized** and **deterministic** versions of the QuickSort algorithm. Perform a comparative analysis of their efficiency by measuring the **average execution time** on arrays of different sizes.

### Technical Requirements

1. Implement the **randomized QuickSort** in a function called `randomized_quick_sort(arr)`, where the pivot element is selected **at random**.
2. Implement the **deterministic QuickSort** in a function called `deterministic_quick_sort(arr)`, where the pivot element is chosen **using a fixed rule** (e.g., first, last, or middle element).
3. Generate test arrays of the following sizes: **10,000**, **50,000**, **100,000**, and **500,000** elements. Fill each array with randomly generated integers.
4. Measure the execution time of both algorithms on each array.  
   To improve measurement accuracy, **repeat the sorting 5 times for each array** and compute the **average execution time**.

---

## Task 2. Scheduling University Lectures Using a Greedy Algorithm

Develop a program to automatically schedule university lectures using a **greedy algorithm** to solve the **set cover problem**.  
The goal is to assign the **minimum number of teachers** necessary to ensure **all subjects are covered**.

---

### Input Data

- **Set of subjects**:  
  `Mathematics`, `Physics`, `Chemistry`, `Computer Science`, `Biology`

- **List of teachers**:

  1. **Oleksandr Ivanenko**, 45 years old  
     Email: `o.ivanenko@example.com`  
     Subjects: `Mathematics`, `Physics`

  2. **Maria Petrenko**, 38 years old  
     Email: `m.petrenko@example.com`  
     Subjects: `Chemistry`

  3. **Serhii Kovalenko**, 50 years old  
     Email: `s.kovalenko@example.com`  
     Subjects: `Computer Science`, `Mathematics`

  4. **Nataliia Shevchenko**, 29 years old  
     Email: `n.shevchenko@example.com`  
     Subjects: `Biology`, `Chemistry`

  5. **Dmytro Bondarenko**, 35 years old  
     Email: `d.bondarenko@example.com`  
     Subjects: `Physics`, `Computer Science`

  6. **Olena Hrytsenko**, 42 years old  
     Email: `o.grytsenko@example.com`  
     Subjects: `Biology`

---

### Implementation Requirements

- Create a data structure for each teacher with the following attributes:
  - First name
  - Last name
  - Age
  - Email
  - Set of subjects they can teach

- Implement functionality to assign teachers to subjects using the following greedy logic:

  1. At each step, select the teacher who can cover the **most remaining uncovered subjects**.
  2. If multiple teachers qualify, prefer the **youngest**.

- The final result should:
  - Include the **minimum number of teachers** required to cover all subjects.
  - List the assigned subjects for each selected teacher.

---

### Expected Outcome

- All listed subjects must be fully covered.
- Teachers should be assigned in a way that reflects a **greedy and optimal** strategy.
- The result must be presented in a **clear and structured** format.

