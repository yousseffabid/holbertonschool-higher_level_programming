#include "lists.h"

/**
 * create_node - creates a new node
 * @number: integer to be included in new node
 * Return: address of the new element
 */
listint_t *create_node(int number)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	new_node->n = number;
	new_node->next = NULL;

	return (new_node);
}

/**
 * *insert_node - inserts a new node in a sorted list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *previous, *new_node;

	if (head == NULL)
		return (NULL);
	if (*head == NULL)
		return (add_nodeint_end(head, number));
	current = *head;
	while (current != NULL)
	{
		if (current->n > number || current->next == NULL)
		{
			new_node = create_node(number);
			if (current == *head)
			{
				new_node->next = current;
				current = new_node;
				*head = current;
				break;
			}
			else
			{
				if (current->n > number)
				{
					new_node->next = current;
					previous->next = new_node;
				}
				else
					current->next = new_node;
				break;
			}
		}
		previous = current;
		current = current->next;
	}
	return (new_node);
}
