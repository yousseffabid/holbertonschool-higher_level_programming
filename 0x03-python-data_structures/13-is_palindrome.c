#include "lists.h"
/**
 * is_palindrome - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: 1 if plindrome or 0 if it is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *prev, *temp;

	if (head == NULL)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	fast = *head;
	slow = *head;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	prev = NULL;
	while (slow)
	{
		temp = slow->next;
		slow->next = prev;
		prev = temp;
		slow = temp;
	}

	temp = *head;
	while (prev)
	{
		if (temp->n != prev->n)
			return (0);
		prev = prev->next;
		temp = temp->next;
	}
	return (1);
}
