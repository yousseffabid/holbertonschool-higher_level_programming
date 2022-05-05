#include "lists.h"

dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *head_ref, *new_node;

	if (head == NULL)
		return (NULL);

	head_ref = *head;
	new_node = malloc(sizeof(dlistint_t));
	if (new_node == NULL)
		return (NULL);

	while (head_ref && head_ref->next)
		head_ref = head_ref->next;

	new_node->next = NULL;
	new_node->prev = head_ref;
	new_node->n = n;

	if (head_ref != NULL)
		head_ref->next = new_node;
	else
		*head = new_node;

	return (new_node);

}
