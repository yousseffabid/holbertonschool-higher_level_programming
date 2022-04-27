#include "lists.h"
/**
 * check_cycle - checks if the list is a cycle
 * @list: pointer to head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	unsigned int number_of_traversal, i;
	listint_t *ptr1, *ptr2, *head;

	if (list == NULL || list->next == NULL)
		return (0);

	ptr1 = list;
	ptr2 =  list;

	while (ptr1 != NULL)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
		if (ptr1 == ptr2)
			return (0);
	}
	return (1);
}

