#include "lists.h"
/**
 * delete_dnodeint_at_index - delete node at index
 * @head: pointer to the head of list
 * @index: index of the node
 * Return: 1 if it succeeded, -1 if it failed
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *prev, *head_ref, *temp;
	unsigned int counter;

	if (head == NULL || *head == NULL)
		return (-1);

	counter = 0;
	head_ref = *head;
	prev = NULL;
	while (head_ref)
	{
		if (index == counter)
		{
			if (index == 0)
			{
				temp = *head;
				*head = (*head)->next;
				free(temp);
				return (1);
			}
			prev->next = head_ref->next;
			head_ref->next->prev = prev;
			free(head_ref);
			return (1);
		}
		counter++;
		prev = head_ref;
		head_ref = head_ref->next;
	}
	return (-1);
}
