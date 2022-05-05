#include "lists.h"
/**
 * print_dlistint - prints all the elements of a list_t list
 * @h: pointer to head of the list
 * Return: number of nodes printed
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t counter;

	if (h == NULL)
		return (0);

	counter = 0;
	while (h)
	{
		printf("%d\n", h->n);
		counter++;
		h = h->next;
	}
	return (counter);
}
