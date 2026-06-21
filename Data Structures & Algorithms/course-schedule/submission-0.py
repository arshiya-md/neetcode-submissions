class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prereq_map = {} # course : list[prereqs] mapping

        for c in range(numCourses):
            prereq_map[c] = [] # Initialize prereqs of each course with []

        # Now append prereqs for each course in map
        for course, preq in prerequisites:
            prereq_map[course].append(preq)

        # Given 'prerequisites' may not necessarily contain all courses, 
        # it may only contain courses with prerequisites
        # therfore to not miss courses with no pre-req, 
        # we are not constructing prereq_map based on given 'Prerequisites' above

        visited = set()

        def dfs(course):
            # If reached already traversed node return
            # It means there is cycle of dependecies return False
            if course in visited:
                return False

            # Base condition
            # If no futher prereqs return
            if prereq_map[course] == []:
                return True

            visited.add(course)

            for preq in prereq_map[course]:
                if not dfs(preq):
                    return False
            visited.remove(course)
            prereq_map[course] = []
            return True


        # DFS of a course C traverses like this (depth wise)
        # -> C's 'first' preq P1 -> P1's 'first' preq P3 -> P3's 'first' preq P4-> 
        # and so on ...-> till no dependencies or breaking condition like
        # reaching an alreay traverses node (means cycle is there)

        # We need to traverse every course because there can be disconnected paths
        # like this A -> B, C-> D
        # If we only traverse from A we can reach B but no C and D
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        
        