#include "lists.h"
/**
 * check_cycle - checks if the list is a cycle
 * @list: pointer to head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	unsigned int number_of_traversal, i;
	listint_t *node_to_check, *current, *head;

	if (list == NULL || list->next == NULL)
		return (0);

	current = list;
	head = list;
	number_of_traversal = 0;
	while (list != NULL)
	{
		node_to_check = list->next;
		number_of_traversal++;
		for (i = 0; i < number_of_traversal; i++)
		{
			if (current == node_to_check)
				return (1);
			current = current->next;
		}
		current = head;
		list = list->next;
	}
	return (0);
}

