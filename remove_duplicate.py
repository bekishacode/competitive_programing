class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
         
          if not head or (head and not head.next):
               return head

          previous = head
          ans = previous
          upcoming = head.next
          while upcoming:
               if previous.val != upcoming.val:
                    previous.next = upcoming
                    previous = previous.next

               else:
                    if previous.next:
                         previous.next = None
               
               upcoming = upcoming.next

          return ans
