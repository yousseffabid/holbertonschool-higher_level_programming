#include "lists.h"
/**
 * insert_dnodeint_at_index - inserts a node at index
 * @h: head of list
 * @idx: index of node
 * @n: data of the node
 * Return: pointer to the inserted node
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *new_node, *head_ref;
	unsigned int counter;

	if (h == NULL)
		return (NULL);

	new_node = malloc(sizeof(dlistint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = n;
	if (*h == NULL)
	{
		*h = new_node;
		new_node->next = NULL;
		new_node->prev = NULL;
		return (new_node);

	}
	counter = 1;
	head_ref = (*h)->next;
	while (head_ref)
	{
		if (counter == idx)
		{
			new_node->next = head_ref;
			new_node->prev = head_ref->prev;
			head_ref->prev->next = new_node;
			head_ref->prev = new_node;
			return (new_node);
		}
		counter++;
		head_ref = head_ref->next;
	}
	return (NULL);
}
