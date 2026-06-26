class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        course_to_preqs = {}

        # Initialize all courses with empty prequisites list
        for course_id in range(numCourses):
            course_to_preqs[course_id] = [] # Empty [] means No prerequisites

        # Now, populate the prereq of courses that has prerequisites
        for course, preq in prerequisites:
            course_to_preqs[course].append(preq)

        current_path = set()
        def can_complete(course_id):
            if course_id in current_path: # There is a cycle so course can't be completed
                return False
            if course_to_preqs[course_id] == []: # No prereqs, so can complete
                return True

            current_path.add(course_id)
            # If there are prereqs then check if each of them can be completed
            for preq in course_to_preqs[course_id]:
                if not can_complete(preq): # Even any of the preqs can't be completed return False
                    return False
            current_path.remove(course_id)

            # Memoize: this course is confirmed to be completable
            course_to_preqs[course_id] = []
            return True

        # If every course can complete then True else False
        for course_id in range(numCourses):
            if not can_complete(course_id):
                return False
        return True
        