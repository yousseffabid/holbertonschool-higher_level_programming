#include "lists.h"
/**
 * get_dnodeint_at_index - get node at index
 * @h: pointer to  head of list
 * @index: index of a node
 * Return: pointer to node at given index
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	unsigned int counter;

	if (head == NULL)
		return (NULL);

	counter = 0;
	while (head)
	{
		if (index == counter)
			return (head);
		counter++;
		head = head->next;
	}
	return (NULL);
}
