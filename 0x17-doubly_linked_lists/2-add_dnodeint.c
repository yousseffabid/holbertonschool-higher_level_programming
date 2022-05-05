#include "lists.h"
/**
 * add_dnodeint - add a new node at the start of the list
 * @head: pointer to head of the list
 * @n: string of the new node
 * Return: address of the inserted node
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *temp, *new_node;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(dlistint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = n;
	temp = *head;
	*head = new_node;
	new_node->prev = NULL;
	new_node->next = temp;

	return (*head);
}
